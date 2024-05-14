from flask import Flask, render_template, session, redirect, request, url_for, jsonify
from flask_socketio import SocketIO, join_room, leave_room  # type: ignore
# from utilities.function import Room, Usertime  # type: ignore
from unogame.logging.log_wrapper import LoggerWrapper
from utilities.function import Usertime  # type: ignore
from unogame.room.room import Room
# import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

logger: LoggerWrapper = LoggerWrapper('logs/latest.log', console=True)
room: Room = Room(log_wrapper=logger)
user_time = Usertime(time_interval=0.1)


def second_clock():
    while True:
        user_time.user_timer_up()
        time.sleep(0.1)


@app.route('/')
def main():
    session.clear()
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def form_room_create():
    if request.method == 'POST':
        room_name = request.form.get('room_name', '')
        user_name = request.form.get('username', '')
        if room_name == '' or user_name == '':
            return redirect(url_for('main'))

        code: str = room.create_room(room_name=room_name, code_length=6, max_user=2)
        player_uuid: str = room.rooms[code].add_user(username=user_name)

        session['UUID'] = player_uuid
        session['Room'] = code
        return redirect(f'/room/{code}')

    return redirect(url_for('main'))


@app.route('/join', methods=['GET', 'POST'])
def form_room_join():
    if request.method == 'POST':
        room_name: str = request.form.get('room_name', '')
        user_name: str = request.form.get('username', '')
        code: str = request.form.get('room_code', '')

        if room_name == '' or user_name == '' or code == '' or room.room_exist(code=code) is False:
            return redirect(url_for('main'))


        player_uuid: str = room.rooms[code].add_user(username=user_name)
        session['UUID'] = player_uuid
        session['Room'] = code
        return redirect(f'/room/{code}')

    return redirect(url_for('main'))


@app.route('/data')
def data():
    return jsonify(room.__dict__())

@app.route('/writefile')
def writefile():
    room.__write__('saved/sample.json')
    return '<h1>File Written</h1>'


@app.route('/room/<code>')
def room_code(code):
    if session.get('UUID') is None or room.room_exist(code) is False:
        return redirect(url_for('main'))

    if room.rooms[code].user_exist(user_uuid=session.get('UUID', 'Null')):
        return render_template("room.html", code=code, title=room.rooms[code].room_name)

    else:
        return redirect(url_for('main'))


@socketio.on('room join')
def room_join():
    session_room = session.get('Room', '')
    session_uuid = session.get('UUID', '')
    if session_room == '' or session_uuid == '' or room.room_exist(session_room) is False:
        return


    join_room(session_room)
    join_room(session_uuid)
    socketio.emit('member_list', room.rooms[session_room].members_list, to=session['Room'])
    socketio.emit('message_history', room.rooms[session_room].message_history, to=session['UUID'])


@socketio.on('room messages')
def handle_message(message):
    session_room = session.get('Room', '')
    session_uuid = session.get('UUID', '')
    if session_room == '' or session_uuid == '' or room.room_exist(session_room) is False:
        return

    message_dict: dict | None = room.rooms[session_room].add_message(session_uuid, message)
    if message is None:
        return

    socketio.emit('message_history', [message_dict], to=session['Room'])

@socketio.on('ping_server')
def ping_server(message):
    if rooms.room_exist(session.get('Room', False)) is False:
        return None

    match message:
        case 'member_list':
            print(rooms.get_room_members_list(session['Room']))

        case 'shuffle_cards':
            rooms.rooms[session['Room']]['UnoData'].shuffle_cards()


@socketio.on('disconnect')
def room_leave():
    if rooms.room_exist(session.get('Room', None)):
        is_room_deleted: bool | None = rooms.remove_player(session['Room'], session['UUID'])
        if is_room_deleted is False:
            socketio.emit("member_list", rooms.get_room_members(session['Room']), to=session['Room'])
        leave_room(session['Room'])
        leave_room(session['UUID'])


if __name__ == '__main__':
    # threading.Thread(target=second_clock).start()
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True, host='0.0.0.0') # type: ignore

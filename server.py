from flask import Flask, render_template, session, redirect, request, url_for, jsonify
from flask_socketio import SocketIO, join_room, leave_room  # type: ignore
from utilities.function import Room, Usertime
# import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

rooms = Room()
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
        code: str = rooms.create_room(request.form['room_name'])
        player_uuid: str = rooms.add_player(code, request.form['username'])

        session['UUID'] = player_uuid
        session['Room'] = code
        return redirect(f'/room/{code}')

    return redirect(url_for('main'))


@app.route('/join', methods=['GET', 'POST'])
def form_room_join():
    if request.method == 'POST':
        code: str = request.form['room_code']
        if rooms.room_exist(code):
            player_uuid: str = rooms.add_player(code, request.form['username'])
            session['UUID'] = player_uuid
            session['Room'] = code
            return redirect(f'/room/{code}')
        else:
            return redirect(url_for('main'))

    return redirect(url_for('main'))


@app.route('/data')
def data():
    return jsonify(rooms.__dict__())

@app.route('/writefile')
def writefile():
    rooms.write_file('saved/sample.json')
    return '<h1>File Written</h1>'


@app.route('/room/<code>')
def room(code):
    if session.get('UUID') is None:
        return redirect(url_for('main'))

    if rooms.room_exist(code) and rooms.room_member_exist(code, session.get('UUID', 'Null')):
        return render_template("room.html", code=code, title=rooms.get_room_name(code))

    else:
        return redirect(url_for('main'))


@socketio.on('room join')
def room_join():
    if rooms.room_exist(session.get('Room', False)):
        join_room(session['Room'])
        join_room(session['UUID'])
        socketio.emit('member_list', rooms.get_room_members(session['Room']), to=session['Room'])
        socketio.emit('message_history', rooms.get_message_history(session['Room']), to=session['UUID'])


@socketio.on('room messages')
def handle_message(message):
    if rooms.room_exist(session.get('Room', False)):
        socketio.emit('message_history', [rooms.add_message(session['Room'], session['UUID'], message)], to=session['Room'])

@socketio.on('ping_server')
def ping_server(message):
    if rooms.room_exist(session.get('Room', False)) is False:
        return None

    match message:
        case 'member_list':
            print(rooms.get_room_members_list(session['Room']))

        case 'shuffle_cards':
            rooms.rooms[session['Room']]['UnoData'].shuffle_cards()

@socketio.on('member_list')
def member_list():
    if rooms.room_exist(session.get('Room', False)):
        print(rooms.get_room_members_list(session['Room']))

@socketio.on('shuffle cards')
def shuffle_cards():
    if rooms.room_exist(session.get('Room', False)):
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

from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

localConfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'dbdesign',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}


def get_db_connection():
    connection = pymysql.connect(**localConfig)
    return connection


@app.route('/')
# 这个没p用，但是为了学习就留着了
# 这里定义的路由是根路径 /，意味着当用户访问你的 Flask 应用的基础 URL（只是localhost+端口或url刚输入）时，这个路由就会被匹配
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM staff WHERE sid = %s AND spassword = %s", (username, password))
        user = cursor.fetchone()
        connection.close()
        if user:
            session['user'] = user
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/home')
def home():
    if 'user' in session:
        user = session['user']
        return render_template('home.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/staff_management', methods=['GET', 'POST'])
def staff_management():
    if 'user' in session:
        user = session['user']
        connection = get_db_connection()
        cursor = connection.cursor()
        if request.method == 'POST':
            sid = request.form['sid']
            sname = request.form['sname']
            ssex = request.form['ssex']
            spassword = request.form['spassword']
            srole = request.form['srole']
            sidcard = request.form['sidcard']
            sphone = request.form['sphone']
            cursor.execute(
                "INSERT INTO staff (sid, sname, ssex, spassword, srole, sidcard, sphone) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (sid, sname, ssex, spassword, srole, sidcard, sphone))
            connection.commit()
            flash('Staff added successfully!', 'success')

        cursor.execute("SELECT * FROM staff")
        staff = cursor.fetchall()
        connection.close()
        return render_template('staff.html', user=user, staff=staff)
        # !!! # 将user & staff数据传递给模板进行渲染
    else:
        return redirect(url_for('login'))

@app.route('/staff_d', methods=['GET', 'POST'])
def staff_d():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        sid = request.form['staff_delete']
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM staff WHERE sid = %s", (sid,))
            connection.commit()
            flash('Staff deleted successfully!', 'success')

        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            connection.close()
        return redirect(url_for('staff_d'))

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM staff")
    staff = cursor.fetchall()
    connection.close()
    return render_template('staff.html', staff=staff)


@app.route('/room')
def room():
    if 'user' in session:
        user = session['user']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM room")
        room = cursor.fetchall()

        connection.close()
        # 获取房间信息的逻辑
        return render_template('room.html', rooms=room)
    else:
        return redirect(url_for('login'))


@app.route('/report')
def report():
    if 'user' in session:
        user = session['user']
        # 获取报表信息的逻辑
        return render_template('report.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/modify_password', methods=['GET', 'POST'])
def modify_password():
    if 'user' in session:
        user = session['user']
        print(user)
        if request.method == 'POST':
            old_password = request.form['old_password']
            new_password = request.form['new_password']

            # 验证旧密码
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT spassword FROM staff WHERE sid = %s", (user['sid'],))
            data = cursor.fetchone()
            connection.close()

            if data:
                print(f"Database password: {data['spassword']}")
                if data['spassword'] == old_password:
                    # 更新密码
                    connection = get_db_connection()
                    cursor = connection.cursor()
                    cursor.execute("UPDATE staff SET spassword = %s WHERE sid = %s", (new_password, user['sid']))
                    connection.commit()
                    connection.close()

                    flash('Password updated successfully!', 'success')
                else:
                    flash('Old password is incorrect.', 'danger')
            else:
                flash('User not found.', 'danger')

        return render_template('modify_password.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/room_management', methods=['GET', 'POST'])
def room_management():
    if 'user' in session:
        user = session['user']
        connection = get_db_connection()
        cursor = connection.cursor()

        if request.method == 'POST':
            rid = request.form['rid']
            rtype = request.form['rtype']
            rprice = request.form['rprice']
            rdesc = request.form['rdesc']
            cursor.execute(
                "INSERT INTO room (rid, rtype, rprice, rdesc) VALUES (%s, %s, %s, %s)",
                (rid, rtype, rprice, rdesc))
            connection.commit()
            flash('Staff added successfully!', 'success')

        cursor.execute("SELECT * FROM room")
        rooms = cursor.fetchall()
        connection.close()
        return render_template('room.html', user=user, rooms=rooms)
    else:
        return redirect(url_for('login'))


@app.route('/room_d', methods=['GET', 'POST'])
def room_d():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        rid = request.form['rid_delete']
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM room WHERE rid = %s", (rid,))
            connection.commit()
            flash('Room deleted successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            connection.close()
        return redirect(url_for('room'))

    # GET 请求：显示删除房间的表单
    return render_template('room.html')

@app.route('/room_mod', methods=['GET', 'POST'])
def room_mod():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            rid = request.form['rid_modify']
            column = request.form['column_modify']
            value = request.form['value_modify']
        except KeyError:
            flash('Missing form data', 'error')
            return redirect(url_for('room'))

        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(f"UPDATE room SET {column} = %s WHERE rid = %s", (value, rid))
            connection.commit()
            flash('Room modified successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            connection.close()
        return redirect(url_for('room'))

    return render_template('room.html')




import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_chart(data, chart_type='line', title='Chart', labels=None):
    fig, ax = plt.subplots()
    if chart_type == 'line':
        ax.plot(data['x'], data['y'])
    elif chart_type == 'bar':
        ax.bar(data['x'], data['y'])
    elif chart_type == 'pie':
        ax.pie(data['y'], labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def get_revenue_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT DATE(end_time) as date, SUM(money) as revenue
        FROM hotelorder
        WHERE end_time >= CURDATE() - INTERVAL 7 DAY
        GROUP BY DATE(end_time)
        ORDER BY DATE(end_time)
    """)
    data = cursor.fetchall()
    connection.close()
    return {
        'x': [d['date'].strftime('%Y-%m-%d') for d in data],
        'y': [d['revenue'] for d in data]
    }


def get_occupancy_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) as total_rooms FROM room")
    total_rooms = cursor.fetchone()['total_rooms']
    cursor.execute("""
        SELECT DATE(start_time) as date, COUNT(DISTINCT rid) as occupied_rooms
        FROM checkin_client
        WHERE start_time >= CURDATE() - INTERVAL 7 DAY
        GROUP BY DATE(start_time)
        ORDER BY DATE(start_time)
    """)
    data = cursor.fetchall()
    connection.close()
    return {
        'x': [d['date'].strftime('%Y-%m-%d') for d in data],
        'y': [(d['occupied_rooms'] / total_rooms) * 100 for d in data]
    }

def get_client_stats_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(DISTINCT cid) as clients FROM checkin_client")
    clients = cursor.fetchone()['clients']
    cursor.execute("SELECT COUNT(DISTINCT tid) as teams FROM checkin_team")
    teams = cursor.fetchone()['teams']
    connection.close()
    return {
        'x': ['Clients', 'Teams'],
        'y': [clients, teams]
    }

def get_staff_performance_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT register_sid as staff, COUNT(*) as orders
        FROM hotelorder
        GROUP BY register_sid
        ORDER BY COUNT(*) DESC
    """)
    data = cursor.fetchall()
    connection.close()
    return {
        'x': [d['staff'] for d in data],
        'y': [d['orders'] for d in data]
    }

@app.route('/report_management')
def report_management():
    if 'user' in session:
        user = session['user']

        revenue_data = get_revenue_data()
        revenue_chart = generate_chart(revenue_data, chart_type='line', title='Revenue in Last 7 Days')

        occupancy_data = get_occupancy_data()
        occupancy_chart = generate_chart(occupancy_data, chart_type='line', title='Occupancy Rate in Last 7 Days')

        client_stats_data = get_client_stats_data()
        client_stats_chart = generate_chart(client_stats_data, chart_type='pie', title='Client Statistics', labels=client_stats_data['x'])

        staff_performance_data = get_staff_performance_data()
        staff_performance_chart = generate_chart(staff_performance_data, chart_type='bar', title='Staff Performance')

        return render_template('report.html', user=user, revenue_chart=revenue_chart, occupancy_chart=occupancy_chart, client_stats_chart=client_stats_chart, staff_performance_chart=staff_performance_chart)
    else:
        return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)

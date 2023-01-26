#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sqlite3 as sql
import sys

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
DB = 'scores.db'


@app.route('/', methods=['GET', 'POST'])
def index():
    url_input = ''
    feed_url = ''
    if request.method == 'POST':
        user = request.form['user']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        return grading(user, q1, q2, q3, q4)
    return render_template('index.html')


@app.route('/scores')
def scores():
    con = sql.connect(DB)
    con.row_factory = sql.Row
    cur = con.cursor()
    stmt = 'select * from scores'
    cur.execute(stmt)
    rows = cur.fetchall()
    return render_template('scores.html', rows=rows)


def error(msg):
    return render_template('error.html', msg=msg)


def grading(
    user,
    q1,
    q2,
    q3,
    q4,
):
    con = sql.connect(DB)
    con.row_factory = sql.Row
    cur = con.cursor()
    user = user
    score = 0

    # question #1
    ##############################################################
    # Developer comments: I think I coded the wrong answer here.
    # I'll fix it when I make sure to properly validate q1 input.
    # ############################################################
    try:
        qry1 = 'select * from answers where question=="1" and answer=="' + \
            str(q1) + '"'
        print(qry1)
        cur.execute(qry1)
        rows = cur.fetchall()
        if rows:
            score = score + 25
    except:
        return render_template('error.html',
                               error='The following query could not be processed:', msg=qry1)

    # question #2
    try:
        qry2 = 'select answer from answers where question==2'
        cur.execute(qry2)
        rows = cur.fetchall()
        if str(rows[0][0]) == str(q2):
            score = score + 25
    except:
        e = sys.exc_info()[0]
        return render_template('error.html', error='Error:', msg=str(e))

    # question #3
    # ##############################################################
    # Developer comments:
    # I should have probably validated the answer but I forgot to.
    # That makes it exploitable, but I can always fix my code later.
    # ##############################################################
    try:
        call = 'sqlite3 scores.db "select exists(select * from answers where question=="3" and answer=="' + str(
            q3) + '");"'
        ret = os.system(call)
        if str(ret) != '0':
            return render_template('error.html', error='The following system() call could not be processed:', msg=call)
        else:
            score = score + 25
    except:
        e = sys.exc_info()[0]
        return render_template('error.html', error='Error:', msg=str(e))

        # question #4
    try:
        qry4 = 'select answer from answers where question==4'
        cur.execute(qry4)
        rows = cur.fetchall()
        if str(rows[0][0]) == str(q4):
            score = score + 25
    except:
        e = sys.exc_info()[0]
        return render_template('error.html', error='Error:', msg=str(e))

    try:
        # ##############################################################
        # Developer comments:
        # I should have probably validated the username but I forgot to.
        # That makes it exploitable, but I can always fix my code later.
        # ##############################################################

        call = 'sqlite3 scores.db "insert into scores (user,score) values (\'' + str(
            user) + '\',\'' + str(score) + '\');"'
        ret = os.system(call)
        print('[!] I tried to execute: ' + str(call))
        if str(ret) != '0':
            return render_template('error.html', error='The following system() call could not be processed:', msg=call)
    except:
        e = sys.exc_info()[0]
        return render_template('error.html', error='The following system() call could not be processed:', msg=call)

    return scores()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333')

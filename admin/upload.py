import os
import json
from flask import request, render_template, current_app, session
from .admin_app import admin_app
from views.upload import get_dir, create_filename


# 用JQ方式上传
@admin_app.route('/by_ajax', methods=['get', 'post'])
def uploadByAjax():
    if request.method == 'POST':
        file_storage_list = request.files.getlist('file')
        message = {'result': '', 'error': '', 'filepath_list': []}
        print(file_storage_list)
        print(request.content_length)  # 上传长度
        if request.content_length > 10240 * 1024:
            message['result'] = 'fail'
            message['error'] = '上传所有文件太大'
            return json.dumps(message)
        for file_storage in file_storage_list:
            print(file_storage.content_type)  # 上传类型
            # 如果上传类型不在允许的类型内，则返回403错误
            if file_storage.content_type not in current_app.config['ALLOW_UPLOAD_TYPE']:
                message['result'] = 'fail'
                message['error'] = '上传文件类型不对'
                return json.dumps(message)
            print(file_storage.filename)  # 上传原文件名
            file_path = os.path.join(get_dir(), create_filename(file_storage.filename))
            try:
                file_storage.save(file_path)
            except Exception as e:
                message = {'result': 'fail', 'error': str(e)}
                return json.dumps(message)
            # [1:]将.static/相对路径转为/static绝对路径
            print(file_path)
            print(file_path[1:])
            message['filepath_list'].append(file_path[1:])
        message['result'] = 'success'
        return json.dumps(message)
    return render_template('admin/upload/jquery_upload.html')


# 用表单方式上传
@admin_app.route('/by_form', methods=['get', 'post'])
def uploadByForm():
    if request.method == 'POST':
        file_storage_list = request.files.getlist('file')
        print(file_storage_list)
        print(request.content_length)  # 上传长度
        if request.content_length > 10240 * 1024:  # 如果上传数据长度大于10M，则返回403错误
            return "", 403
        for file_storage in file_storage_list:
            print(file_storage.content_type)  # 上传类型
            # 如果上传类型不在允许的类型内，则返回403错误
            if file_storage.content_type not in current_app.config['ALLOW_UPLOAD_TYPE']:
                return "", 403
            print(file_storage.filename)  # 上传原文件名
            file_path = os.path.join(get_dir(), create_filename(file_storage.filename))
            file_storage.save(file_path)
    return render_template('admin/upload/form_upload.html')


# 用XHR方式上传
@admin_app.route('/by_xhr', methods=['get', 'post'])
def uploadByXhr():
    if request.method == 'POST':
        file_storage_list = request.files.getlist('file')
        message = {'result': '', 'error': '', 'filepath_list': []}
        print(file_storage_list)
        print(request.content_length)  # 上传长度
        if request.content_length > 10240 * 1024:
            message['result'] = 'fail'
            message['error'] = '上传所有文件太大'
            return json.dumps(message)
        for file_storage in file_storage_list:
            print(file_storage.content_type)  # 上传类型
            # 如果上传类型不在允许的类型内，则返回403错误
            if file_storage.content_type not in current_app.config['ALLOW_UPLOAD_TYPE']:
                message['result'] = 'fail'
                message['error'] = '上传文件类型不对'
                return json.dumps(message)
            print(file_storage.filename)  # 上传原文件名
            file_path = os.path.join(get_dir(), create_filename(file_storage.filename))
            try:
                file_storage.save(file_path)
            except Exception as e:
                message = {'result': 'fail', 'error': str(e)}
                return json.dumps(message)
            # [1:]将.static/相对路径转为/static绝对路径
            print(file_path)
            print(file_path[1:])
            message['filepath_list'].append(file_path[1:])
        message['result'] = 'success'
        return json.dumps(message)
    return render_template('admin/upload/xhr_upload.html')

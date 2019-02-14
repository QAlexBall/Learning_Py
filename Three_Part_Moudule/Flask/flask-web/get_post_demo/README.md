### get请求和post请求
1. get请求:
* 使用场景: 只对服务器获取数据,没有改变服务器数据
* 传参: get请求传参放在url中,通过`?`指定key和value
2. post请求
* 使用场景: 例如登录操作
* 传参: post请求传参不放在url中,通过`from data`的形式发送给服务器

### get和post请求获取参数
1. get请求通过`flask.request.args`获取
2. post请求通过`flask.request.form`获取
3. post请求:
* input标签中,通过name标识value的key
* 写表单时,指定`method='post'`,并要指定`action='/login'`
4. form
```html
<form action="{{ url_for('login') }}" method="post">
    <table>
        <tbody>
            <tr>
                <td>username: </td>
                <td><input type="text" placeholder="please enter username" name="username"></td>
            </tr>
            <tr>
                <td>password: </td>
                <td><input type="text" placeholder="please enter password" name="password"></td>
            </tr>
            <tr>
                <td></td>
                <td><input type="submit" value="login"></td>
            </tr>
        </tbody>

    </table>
</form>
```
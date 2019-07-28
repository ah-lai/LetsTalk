function register(username, password) {
    $.post('user/', '{"username": "' + username + '", "password": "' + password + '"}',
        function (data) {
            //console.log(data);
            window.location = '/';
        }).fail(function (response) {
            $('#id_username').addClass('invalid');
        })
}
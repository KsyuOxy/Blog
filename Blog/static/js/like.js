$(document).ready( function () {

    $('#like_button').click(function () {
        console.log('likes work')

        if ($(this).text() === ':)'){
            $(this).text(':) LIKED')
            $(this).attr('class', 'btn btn-success btn-sm')

            $.ajax(url:{
                url: '/forum/{{post.id}}/like',
                method: 'GET',
                data: {
                    'like_action': 'add',
                    'user': '{{user}}'
                },
                success: function (result) {
                    console.log('like ok')
                }
            })

        }else{
            $(this).text(':)')
            $(this).attr('class', 'btn btn-outline-success btn-sm')
        }
    })
})


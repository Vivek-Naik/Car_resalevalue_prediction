const get = elem => document.getElementById(elem),
					 registerButton = get('register'),
					 loginButton = get('login'),
					 container = get('container')
 
registerButton.onclick = () => {
					 container.className = "active"
}

loginButton.onclick = () => {
						container.className = "close"
}
document.getElementById('logout-button').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('logout-form').submit();
});
$(document).ready(function() {
    $('#register').click(function() {
        $('.front').addClass('flip');
        $('.back').addClass('flip');
    });

    $('#login').click(function() {
        $('.front').removeClass('flip');
        $('.back').removeClass('flip');
    });
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

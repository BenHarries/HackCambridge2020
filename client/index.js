var span = document.getElementById('phrase'),
    text = span.innerHTML.split('').map(function(el) {
        return '<span class="char-' + el.toLowerCase() + '">' + el + '</span>';
    }).join('');

span.innerHTML = text;
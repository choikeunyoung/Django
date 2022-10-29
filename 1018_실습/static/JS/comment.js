const commentBtn = document.querySelector("#submitBtn");
commentBtn.addEventListener('click',function(){
    const formVal = document.querySelector('#valinfo').value;

    let param = {
        'userid' : '{{ request.user.pk }}',
        'articleid' : '{{ form.pk }}',
        'content' : formVal,
    }
    $.ajax({
        url : '{% url "prac:comment_create"  %}'
    })
});
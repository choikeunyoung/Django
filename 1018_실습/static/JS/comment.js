const commentForm = document.querySelector('#comment-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
commentForm.addEventListener('submit', function (event){
    event.preventDefault()
    const userId = event.target.dataset.commentId
    axios({
        method:'post',
        url:`/comments/${userId}/`,
        headers: {'X-CSRFToken': csrftoken,},
        data: new FormData(commentForm)
    })
    .then(response => {
        console.log(response.data)
        const comment = document.querySelector("#comment")
        const h3 = document.createElement("h3")
        h3.innerText = `${response.data.userName}`
        const hr = document.createElement("hr")
        const p = document.createElement("p")
        p.classList.add("text_detail")
        p.innerText = `${response.data.content}`
        comment.append(h3,hr,p)
        commentForm.reset()
    })
})
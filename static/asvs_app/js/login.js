

var form = document.getElementById("login_form")



form.addEventListener('submit',async event => {
    event.preventDefault();

    const data = new FormData(form);
    // data.append('csrfmiddlewaretoken', $('#csrf-helper input[name="csrfmiddlewaretoken"]').attr('value'));
    // let headers = new Headers();
    // // add header from cookie
    // const csrftoken = Cookies.get('csrftoken');
    // headers.append('X-CSRFToken', csrftoken);
    try{
    const res = await fetch("authentication/user/login/",{
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            // "X-CSRFToken": '{%csrf_token%}'
          },
        credentials:"same-origin",
        method:"POST",
        body:JSON.stringify({
            "email":form.email.value,
            "password":form.password.value
        })
    }).then((response)=>{
        if (response.status===200){
        Toastify({
            text: "Login Successfull",
            duration: 3000,
            newWindow: true,
            close: true,
            gravity: "top", // `top` or `bottom`
            position: "center", // `left`, `center` or `right`
            stopOnFocus: true, // Prevents dismissing of toast on hover
            style: {
              background: "linear-gradient(to right, #00b09b, #96c93d)",
              height:"50px"
            }// Callback after click
          }).showToast();
     setTimeout(changepage,4000)
        }
    })
    // const resdata = await res.json();
}
catch(err){
    console.log("err",err)
}

});

function changepage(){
    window.location.assign("/")
}
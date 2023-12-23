

var form = document.getElementById("signup_form")


form.addEventListener('submit',async event => {
    
// console.log(form.referral_code.value)
    event.preventDefault();
    try{
    const res = await fetch("authentication/user/registration/",{
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            // "X-CSRFToken": '{%csrf_token%}'
          },
        credentials:"same-origin",
        method:"POST",
        body:JSON.stringify(
            {"user":
            {
            "email":form.email.value,
            "password":form.password.value,
            "username":form.username.value,
            "name":form.name.value,
            "referral_code":form.referral_code.value

        }})
    }).then((response)=>{
        if (response.status === 201){
            window.location.assign("/")
        }
        if (response.status===400){
            console.log("email")
        }
    }).catch((e)=>{
        console.log(e)
    })
    // const resdata = await res.json();
    // console.log(resdata)
}
catch(err){
    console.log("err",err)
}

});
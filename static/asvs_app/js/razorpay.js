
const handler=((res)=>{

    var data = {
    "order_id":res?.razorpay_order_id,
    "payment_id":res?.razorpay_payment_id,
    "signature_id":res?.razorpay_signature,
    "status":true,    
    }

    try{
        const res = fetch("paymentstatus/",{
            method:"POST",
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
              },
        })
        const resdata = res.json();
        console.log("resdata",resdata)
    }
    catch(err){
        console.log("err",err)
    }

})

function checkout(order_id,amount){
    debugger;
    razorpay_key_id = "rzp_test_G41sFJ3BylKw3u"
    var options = {
        "key": razorpay_key_id, // Enter the Key ID generated from the Dashboard
        "amount": amount, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise or INR 500.
        "currency": "INR",
        "name": "Amar Shanti Vikas Sanstha",
        "description": "Donation",
        "image": "{{logo}}",
        "order_id": order_id,//This is a sample Order ID. Create an Order using Orders API. (https://razorpay.com/docs/payment-gateway/orders/integration/#step-1-create-an-order). Refer the Checkout form table given below
        "handler": function (response){
            handler(response)
            window.location.assign("/")
        }
    };
    var rzp1 = new window.Razorpay(options);
    rzp1.open();
    // e.preventDefault();
}



var form = document.getElementById("donate_form")

form.addEventListener('submit',async event => {
    event.preventDefault();

    const data = new FormData(form);
    const res = await fetch("createpayment/",{
        method:"POST",
        body:data
    }).then((response)=>{
        console.log(response)
        if(response.status===200){
        Toastify({
            text: "Payment Successfull",
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
          console.log("response",response)
           return response.json();
          
        
        }
    }).then((resData) => {
        console.log("resData",resData)
        debugger;
        checkout(resData?.order_id,resData?.amount)
    })
    .catch((err)=>{
        console.log("error",err)
    })


})
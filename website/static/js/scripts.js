$('.plus-cart').click(function(){
    console.log('Button clicked')

    var id = $(this).attr('pid').toString()
    var quantity = this.parentNode.children[2]

    $.ajax({
        type: 'GET',
        url: '/pluscart',
        data: {
            cart_id: id
        },
        
        success: function(data){
            console.log(data)
            quantity.innerText = data.quantity
            document.getElementById(`quantity${id}`).innerText = data.quantity
            document.getElementById('amount_tt').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total

        }
    })
})



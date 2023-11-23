let btn_minus=document.getElementById('btn_minus')
 btn_minus.addEventListener('click',( )=> {
    let qty_input = document.getElementById('qty')
    qty = qty_input.value

    if (qty >=2) {
        qty--
    }
    qty_input.value = qty
})

let btn_plus = document.getElementById('btn_plus')

btn_plus.addEventListener('click',() => {
    let qty_input = document.getElementById('qty')
    qty = qty_input.value
    
    qty++
    qty_input.value = qty
})
 


let mithai= document.getElementById('gifting')
mithai.addEventListener('click',()=>{
  gifting_div=document.getElementById('gifting_div');
  gifting_div.classList.add('d-none')
  
})



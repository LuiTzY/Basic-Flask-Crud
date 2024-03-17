const btnDelete = document.querySelectorAll('.btn-delete')
console.log(btnDelete)
if(btnDelete){
    const btnArr = Array.from(btnDelete)
    btnArr.forEach((btn)=>{
        btn.addEventListener(('click'), (e)=>{
            if(!confirm("Estas seguro de eliminar el contacto? ")){
                e.preventDefault(); 
            }
        })
    })
}
const todoObjectList=[];

class Todo_Class{
    constructor(item){
        this.ulElement=item;
    }

    add(){
        const todoInput=document.querySelector("#myInput").value;
        if (todoInput==""){ //if input is empty string invoke alert
            alert("You did not enter any item!")
        }else{ //if input is not empty assign the element going to stoerd in array an id,text(what is being written),and done(checked out in case it is done ,by default value is false)
            const todoObject={
                id:todoObjectList.length,
                todoText:todoInput,
                isDone:false,
            }
        
        todoObjectList.unshift(todoObject);
        this.display();
        document.querySelector("#myInput").value='';
        }
    }

    done_undone(x){//id sent from display to check if done or undone
        const selectedTodoIndex=todoObjectList.findIndex((item)=>item.id==x);//assign index number of object,findindex finds specific index number in array,parameters in brackets specify what we are looking for
        console.log(todoObjectList[selectedTodoIndex].isDone);//logs in the console the value of is done if it is true or not
        todoObjectList[selectedTodoIndex].isDone==false?todoObjectList[selectedTodoIndex].isDone=true:todoObjectList[selectedTodoIndex].isDone=false;//checks the isDone value of the selected index of the array if it is done portray true and vice versa
        this.display();//invoke this feature on display
    }

    deleteElement(z){
        const selectedDelIndex=todoObjectList.findIndex((item)=>item.id==z);//attain the index value an trigger the delete characteristics
        todoObjectList.splice(selectedDelIndex,1);//splice method deletes object in the array whose index is selected
        this.display();
    }

    display(){
        this.ulElement.innerHTML="";//for claening the content of list at beginning,to avoid repetiton of items on user's clicks
        todoObjectList.forEach((object_item)=>{//loops for every element in the array
            const liElement=document.createElement("li");//takes in text as input
            const delBtn=document.createElement("i");//adds trash icon with every incoming text

            liElement.innerText=object_item.todoText;//assign id property to text
            liElement.setAttribute("data-id",object_item.id);

            delBtn.setAttribute("data-id",object_item.id);//assign id property to trash button
            delBtn.classList.add("far","fa-trash-alt");//add two class names to make it appear as trash can

            liElement.appendChild(delBtn);//add the trash can button after the text

            delBtn.addEventListener("click",function(e){//adding event listener to every trash button so that it deletes the selected object from the array
                const deleteId=e.target.getAttribute("data-id");//brings us the id value to be deleted
                myTodoList.deleteElement(deleteId);//delets the fetched id
            })

            liElement.addEventListener("click",function(e){//attain the id value for every element in array
                const selectedId=e.target.getAttribute("data-id");//fethc the selected id
                myTodoList.done_undone(selectedId);//pass the selected Id to done_undone function
            })

            if (object_item.isDone){//add checked===true for the class items whose isDone property is true
                liElement.classList.add("checked");
            }
            this.ulElement.appendChild(liElement);//for displaying the liElement id on the screen
        })

    }
}

const listSection=document.querySelector("#myUL");
myTodoList=new Todo_Class(listSection);

document.querySelector(".addBtn").addEventListener("click",function(){
    myTodoList.add()
})

document.querySelector("#myInput").addEventListener("keydown", function(e) {
    if (e.keyCode == 13) {
        myTodoList.add()
    }
})




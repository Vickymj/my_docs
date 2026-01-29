<!-- import { useState } from "react"

function ChatInput(){
    <div>
        <input></input>
        <input />
        <button>Send</button>
    </div>
}
const div = (
    <div>
        {ChatInput()}
        <ChatInput></ChatInput> //Compent syntax
        <ChatInput />
    </div>

    fragment used to do group element <></>
)

PrOPS

function ChatInput(props){
    console.log(props)
    const sender= props.sender
    const {sender} = props  #Destructing
    const {message, sender} = props  #Destructing
    <>
    {}
        <input />
        <button>Send</button>
    </>
}
const div = (
    <>
        <ChatInput message="hello world" sender="robot"/>
    </>)


function ChatInput({message, sender}) %%% inportant
{
    return (
        <>
        {if sender == "robot"}  // we cannot user if  here so use guard operator (const result = value1 && value2)
         if value1 true then result will be value2
        {   }
            {message}
            {sender}
        </>
    )
    
}

const datas = [{
    message : "hello world",
    sender : "sender"
},
    {
    message : "how are you",
    sender : "robot"
}
]

datas.push(
   {
    message : "I need help",
    sender : "sender"
} 
)

datas.map(()=>{

})

const chatMessageComponet =datas.map((data)=>{
   return (
    //<ChatInput message="hello world" sender="robot"/>
    <ChatInput message={datas.message} sender={datas.sender} />
   ) 
})



useState dont use push

const array = React.useState([{
    message : "hello world",
    sender : "sender"
},
    {
    message : "how are you",
    sender : "robot"
}
])

// const chatMessage = array[0] // current data
// const setChatMessage =  array[1] //updater functions

//array destruction
// const [chatMessage, setChatMessage] = array

const [chatMessage, setChatMessage]  = React.useState([{
    message : "hello world",
    sender : "sender"
},
    {
    message : "how are you",
    sender : "robot"
}
])




setChatMessage([
    ...chatMessage,  {
    message : "I need help",
    sender : "sender",
    id : crypto.randomUUID()
} 
])




spread operator (...)

lifting state Up

Named export
default export -->

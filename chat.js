async function sendMessage(){
 const message=document.getElementById('message').value;
 const response=await fetch('/chat',{
   method:'POST',
   headers:{'Content-Type':'application/json'},
   body:JSON.stringify({message})
 });
 const data=await response.json();
 document.getElementById('chat-box').innerHTML +=
   `<p><b>用户:</b> ${message}</p><p><b>AI:</b> ${data.response}</p>`;
}

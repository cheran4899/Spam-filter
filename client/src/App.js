import React, {useState, useEffect} from 'react';
import './Form.css';

function App() {

  const [data, setData] = useState({})


  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, []);

  
  return (


<body>
  
<div className = "form-box"> 
<h5 className='form-heading'>Spam Detection</h5>
<form>
<div>
<input placeholder='Paste your email content to analyse' type='text' value={data} onChange={e => setData(e.target.value)}/>
</div>
<div>
<button className='f_button' 
type='submit'
value="add todo"
onClick={ async () => {

  const todo = {data}
  const response = await fetch("/input",{
    method : "POST",
    headers : {
      'Content-Type' : 'application/json'
    },
    body: JSON.stringify(todo)
  })
  

}}>
click hear to send data 
</button>

</div>

</form>
</div>


</body>
  );
}

export default App;

import React, {useState} from 'react';
import './Form.css';
import axios from 'axios';

function App() {

  const [data, setData] = useState({})
  const [resp, getResp] = useState({});


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
  await axios.post("/input",{
    headers : {
      'Content-Type' : 'application/json'
    },
    body: JSON.stringify(todo)
  })
  .then((response) => {
    getResp(response.data)
 })
 .then((response) => {
  console.log(response.status, response.data)})
}}>
click hear to send data 
</button>

</div>

</form>
</div>

<h5>{resp.message}</h5>

</body>
  );
}

export default App;

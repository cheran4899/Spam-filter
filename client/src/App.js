import React, {useState} from 'react';
import './Form.css';
import axios from 'axios';

function App() {

  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  const handleChange = (event) => {
    setInputText(event.target.value);
  };

  
  const handleClick = () => {
    axios.post('/input', { sentence: inputText })
      .then((response) => setOutputText(response.data.conversion))
      .catch((error) => console.error('Error:', error));
  };

return (
<body>
  
<div className = "form-box"> 
<h5 className='form-heading'>Spam Detection</h5>
<input type="text" value={inputText} onChange={handleChange} />
      <button onClick={handleClick}>Change Case</button>
      <p>{outputText}</p>
</div>


</body>
  );
}

export default App;

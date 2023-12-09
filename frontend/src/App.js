
import './App.css';
import {useState} from 'react' ;
import Axios from 'axios';
import CircleLoader from 'react-spinners/CircleLoader';

function App() {
  const [url ,seturl] = useState("");
  const [promp, setpromp] = useState("");
  const [con,setcon] = useState(false);
  const [ret, setret] = useState("");
  
  const handlesubmit = (e)=>{
    setret([]);
    e.preventDefault();
    setcon(true);
    Axios.postForm("/mess",{
      url:url,
      prompa:promp
    })
    .then(res=>{
      
      console.log(res.data);
      setret(res.data);
    })
    
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <div className="input-button">
          <form  onSubmit={(e)=>handlesubmit(e)}>
            <div className='text-fields'>
            <input type="text" placeholder="https://link/abc" value={url} onChange={(e)=>{seturl(e.target.value)}} id="url" autoComplete="off"/>
            <input type="text" placeholder='Video title' value={promp} onChange={(e)=>{setpromp(e.target.value)} } id="prompt"autoComplete="off"/>
            </div>
            <button className="submit"  >Create Short</button>
            
          </form>
          {con ? (<>{ret.length ? (<div className='card ouput'>{ret.endsWith("mp3") ? (
          <audio controls>
            <source src="output.mp3" type="audio/mp3"/>
          </audio>
          ):ret.endsWith("mp4")?(<video height={600} width={500} style={{margin:-110}} controls={true}>
            <source src="output.mp4" type="video/mp4"/>
          </video>):(<>Invalid file type</>)}</div>):(<div className='card empty' ><CircleLoader className='load' size={100} color='rgb(119, 13, 218)'/></div>)}</>):(<></>)}
        </div>

      </header>
     
    </div>
  );
}

export default App;

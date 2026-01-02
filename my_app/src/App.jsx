import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios';
import cloudcoloricon from './assets/cloud-color-icon.svg'
import suncoloricon from './assets/day-sunny-color-icon.svg'
import daycloudy from './assets/day-cloudy-color-icon.svg'
import raincoloricon from './assets/cloud-rain-color-icon.svg'
import previous from '/home/yacine/wether_app/my_app/src/assets/chevron-direction-left-icon.svg'
import next from '/home/yacine/wether_app/my_app/src/assets/chevron-direction-right-icon.svg'




function App() {
  const [count, setCount] = useState(0)
const [weatherData, setWeatherData] = useState([]);
const[photo,setPhoto]=useState('');
const[actualIndex,setActualIndex]=useState(0);
const[desactPrev,setDesactPrev]=useState(true);
const[desactNext,setDesactNext]=useState(false);
const [backgroundStyle, setBackgroundStyle] = useState('linear-gradient(135deg, #667eea 0%, #764ba2 100%)');


const fetchWeatherData = async () => {
  try {
    const response = await axios.get('http://localhost:8000/predictions')
    const data=typeof response.data ==='string' ? JSON.parse(response.data) : response.data; 
    return data;
    
  } catch (error) {
    console.error(error);
    return [];
  }
};

useEffect(() => {
  const getData = async () => {
    const data = await fetchWeatherData();
    setWeatherData(data);
  };
  getData();
}, []);
useEffect(() => {
  if (weatherData.length > 0) {
    document.body.style.background = getBackgroundStyle(weatherData[actualIndex]);
    document.body.style.transition = 'background 0.5s ease';
  }
}, [actualIndex, weatherData]);
const getWeatherIcon = (weatherData) => {
  if (!weatherData) return null;
  
  const cloudCover = weatherData.cloud_cover_mean;
  const precipitation = weatherData.precipitation_sum;
  
  if (precipitation > 2) {
    return raincoloricon;
  }
  

  if (cloudCover < 30) {
    return suncoloricon;
  }

  if (cloudCover >= 30 && cloudCover < 60) {
    return daycloudy;
  }

  return cloudcoloricon;
};
const desactiver =(who) => {
  if (who==='prev') {
    return true;
}
if (who==='next') {
  return true;
}}

if (actualIndex > 0 && desactPrev) {
  setDesactPrev(false);
}
if (actualIndex < weatherData.length - 1 && desactNext) {
  setDesactNext(false);
}



// console.log('weatherData STATE = ', weatherData);
// console.log('weatherData STATE = ', weatherData);
// console.log('weatherData type = ', typeof weatherData);
// console.log('weatherData est array? = ', Array.isArray(weatherData));
// console.log('weatherData[0] = ', weatherData[0]);
// console.log('typeof weatherData[0] = ', typeof weatherData[0]);
// if (weatherData[0]) {
//   console.log('Keys de weatherData[0] = ', Object.keys(weatherData[0]));
//   console.log('weatherData[0].date = ', weatherData[0].date);
// }
const getBackgroundStyle = (weatherData) => {
  if (!weatherData) return 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
  
  const cloudCover = weatherData.cloud_cover_mean;
  const precipitation = weatherData.precipitation_sum;
  
  if (precipitation > 2) {
    return 'linear-gradient(135deg, #4b6cb7 0%, #182848 100%)';
  }
  
  if (cloudCover < 30) {
    return 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)';
  }

  if (cloudCover >= 30 && cloudCover < 60) {
    return 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)';
  }
  
  return 'linear-gradient(135deg, #bdc3c7 0%, #2c3e50 100%)';
};
  return (

<>
    <div
      className="App"
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'flex-start',
        textAlign: 'left',             
        border: '2px solid black',
        padding: '20px',
        margin: '20px auto',           
        height: '70vh',
        width: '50vh',
        borderRadius: '20px'
      }}
    >
      <div>
        <h2 style={{textAlign:'center'}}>Weather Forecast App</h2>
      </div>
<div className='central' style={{ position:'relative', height:'100%' }}>

  <div className='gauche' style={{ position:'absolute', top:'50%', left:'0', transform:'translateY(-50%)' }}> 
    <button disabled={desactPrev} onClick={ ()=>{
      setActualIndex(e => {
        const newIndex = e - 1;
        if (newIndex <= 0) {
          setDesactPrev(true);
          desactiver('prev');
    }
        return newIndex;
      }
    )

    }}>
      <img src={previous} alt="Previous" />

    </button>
  </div>
  <div className='meteo' style={{ position:'absolute', top:'50%', left:'50%', transform:'translate(-50%, -50%)' ,width:'60%',border:'1px solid gray',borderRadius:'10px',height:'60%',display:'flex',flexDirection:'column',justifyContent:'flex-start'
  }}>
    <div className="date" style={{ textAlign: 'center', marginTop: '10px' }}>
    <h2 style={{color:'green'}}>    {weatherData.length > 0 ? String(weatherData[actualIndex].date) : 'Chargement...'}</h2>

    </div>
    <div className="photo" style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
      <img style={{textAlign:'center',width:'40%'}} src={getWeatherIcon(weatherData.length > 0 ? weatherData[actualIndex] : null)} alt="" />
    </div>
    <div className="temperature"  style={{textAlign:'center'}}> <h2>{weatherData.length > 0 ? `${parseInt(weatherData[actualIndex].temperature_2m_mean, 10)}°C` : ''}</h2></div>


  </div>
  <div className='droite' style={{ position:'absolute', top:'50%', right:'0', transform:'translateY(-50%)' }}>
    <button disabled={desactNext} onClick={ ()=> {
      setActualIndex(e => {
        const newIndex = e + 1;
        if (newIndex >= weatherData.length) {
          setDesactNext(true);
          desactiver('next');

          return e;
      }
        return newIndex;
      }
    )

    }}>
      <img src={next} alt="Next" />

    </button>

  </div>
</div>




    </div>
    

</>
  )
}

export default App

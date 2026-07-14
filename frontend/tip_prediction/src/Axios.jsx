import axios from 'axios';

const BaseUrl = 'https://tipprediction-app-3.onrender.com/'

const Axios = axios.create({
    baseURL: BaseUrl,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
})     
export default Axios 

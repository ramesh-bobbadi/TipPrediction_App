import axios from 'axios';

const BaseUrl = 'http://127.0.0.1:8000/'

const Axios = axios.create({
    baseURL: BaseUrl,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
})     
export default Axios 

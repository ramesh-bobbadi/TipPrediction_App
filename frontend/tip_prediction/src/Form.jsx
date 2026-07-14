import Axios from './Axios'
import React, { useState } from 'react'

function Form() {
    const [udata, setUdata] = useState({total_bill:'', sex:'', day:'', time:'', smoker:''})
    const [prediction, setPrediction] = useState('')
    const handleChange = (e) => setUdata({...udata, [e.target.name]: e.target.value})

    const submithadler = async (e) => {
        e.preventDefault()
        try {
            const response = await Axios.post('tp_data/', udata)
            setPrediction(response.data.predicted_tip)
            console.log(response.data.predicted_tip)

        } catch (error) {
    console.log("========== ERROR ==========");
    console.log(error);

    if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);
    } else if (error.request) {
        console.log("No response received");
        console.log(error.request);
    } else {
        console.log(error.message);
    }
}
    }

    return (
        <div>
            <form onSubmit={submithadler}>
                <label>Total Bill</label>
                <input type='number' name='total_bill' value={udata.total_bill} onChange={handleChange}/>

                <label>Sex</label>
                <select name='sex' value={udata.sex} onChange={handleChange}>
                    <option value=''>Select</option>
                    <option value='Male'>Male</option>
                    <option value='Female'>Female</option>
                </select>

                <label>Day</label>
                <select name='day' value={udata.day} onChange={handleChange}>
                    <option value=''>Select</option>
                    <option value='Thur'>Thur</option>
                    <option value='Fri'>Fri</option>
                    <option value='Sat'>Sat</option>
                    <option value='Sun'>Sun</option>
                </select>

                <label>Time</label>
                <select name='time' value={udata.time} onChange={handleChange}>
                    <option value=''>Select</option>
                    <option value='Lunch'>Lunch</option>
                    <option value='Dinner'>Dinner</option>
                </select>

                <label>Smoker</label>
                <select name='smoker' value={udata.smoker} onChange={handleChange}>
                    <option value=''>Select</option>
                    <option value='Yes'>Yes</option>
                    <option value='No'>No</option>
                </select>

                <button type='submit'>Submit</button>
            </form>
            {prediction && (
                <div>
                    <h3>Prediction_tip: {prediction}</h3>
                </div>
            )}
        </div>
    )
}

export default Form
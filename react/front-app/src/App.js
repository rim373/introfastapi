import React ,{useState,useEffect} from "react";
import api from './api'



const App =() => {
    const [transactions, setTtransactions]=useState([]);
    const [formData, setFormData] = useState({
        amount :'',
        category :'',
        description:'',
        is_income: false,
        date: ''

    });

    const fetchTransactions = async () => {
        const response = await api.get('/');
        setTtransactions(response.data)
    };

    useEffect(()=> {
        fetchTransactions();
    },[]);
    const handleInputChange = (event) => {
        const value = event.target.type === 'chekbox' ? event.target.checked : event.target.value;
        setFormData({
            ...formData,
            [event.target.name]:value,

        });
    };

    const handleFormSubmit = async (event)=>{
        event.preventDefault();
        await api.post('/q',formData)
        fetchTransactions();
        setFormData({
            amount :'',
            category:'',
            description:'',
            is_income:false,
            date:''
        });
    };
    return(
        <div>
            <nav className='navbar navbar-dark bg-primary'>
                <div className = 'container-fluid'>
                    <a className='navbar-brand' href="#">
                        front-app

                    </a>
                </div>

            </nav>
            <div className='container'>
                <form onSubmit={handleFormSubmit}>
                    <div className='mb-3 mt-3'>

                        <label htmlFor='amount' className='form-label'>
                            amount


                        </label>
                        <input type='text' className='form-control' id='amount' id='amount' onChange={handleInputChange} value={formData.amount}/>

                    </div>
                    <div className='mb-3 '>

                        <label htmlFor='category' className='form-label'>
                            CATEGORY


                        </label>
                        <input type='text' className='form-control' id='category' name='category' onChange={handleInputChange} value={formData.category}/>

                    </div>
                </form>
            </div>
        </div>
    )
}



export default App;
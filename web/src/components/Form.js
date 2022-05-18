import React, { useState } from 'react';
import { InputStyles } from '../styles/InputStyles';
import { SelectStyles } from '../styles/SelectStyles';
import { FormStyles } from '../styles/ComponentStyles';

export default function Form({ setUrl }) {
  const [state, setState] = useState({
    description: '',
    amount: 0,
    currency: 'USD',
  });

  function handleChange(e) {
    const { name, value } = e.target;
    console.log(state)
    setState({
      ...state,
      [name]: value,
    });
  }

  function checkFields() {
    if (state.description === '' && state.amount > 0) {
      alert('Invalid Description: Please try again!')
    }
    if (state.amount === 0 && state.description !== '') {
      alert('Invalid Amount: Please try again!')
    }
    if(state.amount === 0 && state.description === ''){
      alert('Invalid Inputs: Please try again!')
    }
  }

  function saveNewSpendingInApi() {
    checkFields()
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        description: state.description,
        amount: state.amount,
        currency: state.currency
      }),
    };
    if(state.description !== '' && state.amount > 0){
      fetch("/api/new-spending", requestOptions)
      .then((response) => response.json())
        .then(setState({
            description: '',
            amount: 0,
            currency: 'USD',
        }))
        .then(setUrl(`http://localhost:8000/api/get-all-spendings`))
    }
  }



  return (
    <>
      <FormStyles>
        <InputStyles
          type='text'
          placeholder='description'
          name='description'
          value={state.description}
          onChange={handleChange}
        />
        <InputStyles
          type='number'
          placeholder='amount'
          name='amount'
          value={state.amount}
          onChange={handleChange}
        />
        <SelectStyles
          name='currency'
          value={state.currency}
          onChange={handleChange}
        >
          <option value='HUF'>HUF</option>
          <option value='USD'>USD</option>
        </SelectStyles>
        <InputStyles type='submit' value='Save' onClick={saveNewSpendingInApi}/>
      </FormStyles>
    </>
  );
}

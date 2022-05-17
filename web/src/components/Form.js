import React, { useState } from 'react';
import { InputStyles } from '../styles/InputStyles';
import { SelectStyles } from '../styles/SelectStyles';
import { FormStyles } from '../styles/ComponentStyles';
import {render} from "react-dom";

export default function Form({ setUrl }) {
  const [state, setState] = useState({
    description: '',
    amount: 0,
    currency: 'USD',
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setState({
      ...state,
      [name]: value,
    });
  }

  function checkFields() {
      if(state.description === '' || state.amount === 0){
        alert('Invalid Input: Please try again!')
      }
    }

  function saveNewSpendingInApi(e) {
    checkFields()
    e.preventDefault()
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        description: state.description,
        amount: state.amount,
        currency: state.currency
      }),
    };
    fetch("/api/new-spending", requestOptions)
      .then((response) => response.json())
        .then(setUrl(`http://localhost:8000/api/get-all-spendings`))
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

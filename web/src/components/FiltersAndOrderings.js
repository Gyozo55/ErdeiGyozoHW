import React, {useState} from 'react';
import { FiltersWrapper, Orderings, CurrencyFilters, CurrencyButton } from '../styles/ComponentStyles';

export default function CurrencyFilter({ spendings, setSpendings }) {

  const [orderState, setOrderState] = useState({
    name : '',
    type : '',
  });

  const [filterState, setFilterState] = useState({
    type : '',
  });

  function handleSortingChange(e) {
    setOrderState({
      name: e.target.name,
      type: e.target.value,
    });
    getOrderedSpendings()
  }

  function getOrderedSpendings() {
    console.log(orderState.type)
    console.log(orderState.name)
    const url = `/api/order-spendings?order-type=${orderState.type}&order-name=${orderState.name}`
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" }};

    fetch(url, requestOptions)
      .then((response) => response.json())
        .then(data => setSpendings(data))
  }

  function getFilteredSpendings() {
    console.log(filterState.type)
    const url = `/api/filter-by-currency?filter-type${filterState.type}`
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" }};

    fetch(url, requestOptions)
      .then((response) => response.json())
        .then(data => setSpendings(data))
  }

  return (
    <>
      <FiltersWrapper>
        <Orderings>
          <select onChange={handleSortingChange}>
            <option name='date' value='DESC'>Sort by Date descending (default)</option>
            <option name='date' value='ASC'>Sort by Date ascending</option>
            <option name='amount' value='DESC'>Sort by Amount descending</option>
            <option name='amount' value='ASC'>Sort by Amount ascending</option>
          </select>
        </Orderings>
        <CurrencyFilters>
          <li>
            <CurrencyButton
              name='ALL'
              onClick={ (e) => {
               getFilteredSpendings();
               setFilterState(e.target.name)
              }}
            >
              ALL
            </CurrencyButton>
          </li>
          <li>
            <CurrencyButton
              name='HUF'
              onClick={ (e) => {
               getFilteredSpendings();
               setFilterState(e.target.name)
              }}
            >
              HUF
            </CurrencyButton>
          </li>
          <li>
            <CurrencyButton
              name='USD'
              onClick={ (e) => {
               getFilteredSpendings();
               setFilterState(e.target.name)
              }}
            >
              USD
            </CurrencyButton>
          </li>
        </CurrencyFilters>
      </FiltersWrapper>
    </>
  );
    // <option name='-date' value='DESC'>Sort by Date descending (default)</option>
    // <option name='date' value='ASC'>Sort by Date ascending</option>
    // <option name='-amount' value='DESC'>Sort by Amount descending</option>
    // <option name='amount' value='ASC'>Sort by Amount ascending</option>
}

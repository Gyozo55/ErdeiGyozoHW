import React, {useEffect, useState} from 'react';
import { FiltersWrapper, Orderings, CurrencyFilters, CurrencyButton } from '../styles/ComponentStyles';


export default function CurrencyFilter({ setSpendings, setUrl }) {

  const [orderState, setOrderState] = useState({
    name : '',
    value : '',
  });

  const [filterState, setFilterState] = useState({
    name : '',
  });

  useEffect ( ()=>{
    setUrl(`http://localhost:8000/api/filter-by-currency?filter-type=${filterState}`)
  }, [filterState])

  useEffect ( ()=>{
    setUrl(`http://localhost:8000/api/order-spendings?order-type=${orderState.value}&order-name=${orderState.name}`)
  }, [orderState])

  function handleSortingChange(e) {
    setOrderState({
      name: e.title,
      value: e.target.value,
    });
  }

  function handleFilterChange(e) {
    setFilterState(e.target.name)
  }

  // async function getOrderedSpendings() {
  //   console.log(orderState.type)
  //   console.log(orderState.name)
  //   const url = `http://localhost:8000/api/order-spendings?order-type=${orderState.value}&order-name=${orderState.name}`
  //   setUrl(url)
  //   // await fetchDataFromApiWithGet(url)
  // }
  //
  // async function getFilteredSpendings() {
  //   console.log(filterState)
  //   const url = `http://localhost:8000/api/filter-by-currency?filter-type=${filterState}`
  //   setUrl(url)
  //   // await fetchDataFromApiWithGet(url)
  // }
  //
  // async function fetchDataFromApiWithGet(url){
  //   const requestOptions = {
  //     method: "GET",
  //     headers: { "Content-Type": "application/json" }};
  //
  //   await fetch(url, requestOptions)
  //     .then((response) => response.json())
  //       .then(data => setSpendings(data))
  // }

  return (
    <>
      <FiltersWrapper>
        <Orderings>
          <select onChange={handleSortingChange}>
            <option title='date' value='DESC'>Sort by Date descending (default)</option>
            <option title='date' value='ASC'>Sort by Date ascending</option>
            <option title='amount' value='DESC'>Sort by Amount descending</option>
            <option title='amount' value='ASC'>Sort by Amount ascending</option>
          </select>
        </Orderings>
        <CurrencyFilters>
          <li>
            <CurrencyButton
              name='ALL'
              onClick={handleFilterChange}
            >
              ALL
            </CurrencyButton>
          </li>
          <li>
            <CurrencyButton
              name='HUF'
              onClick={handleFilterChange}
            >
              HUF
            </CurrencyButton>
          </li>
          <li>
            <CurrencyButton
              name='USD'
              onClick={handleFilterChange}
            >
              USD
            </CurrencyButton>
          </li>
        </CurrencyFilters>
      </FiltersWrapper>
    </>
  );
}

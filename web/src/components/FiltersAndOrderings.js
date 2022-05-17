import React, {useState} from 'react';
import { FiltersWrapper, Orderings, CurrencyFilters, CurrencyButton } from '../styles/ComponentStyles';

export default function CurrencyFilter({ setSpendings }) {

  const [orderState, setOrderState] = useState({
    name : '',
    value : '',
  });

  const [filterState, setFilterState] = useState({
    name : '',
  });

  function handleSortingChange(e) {
    setOrderState({
      name: e.target.name,
      value: e.target.value,
    });
    getOrderedSpendings()
  }

  async function handleFilterChange(e) {
    e.preventDefault()
    console.log(e.target.name)
    setFilterState(e.target.name)
    console.log(filterState.name)
    await getFilteredSpendings();
  }

  async function getOrderedSpendings() {
    console.log(orderState.type)
    console.log(orderState.name)
    const url = `/api/order-spendings?order-type=${orderState.value}&order-name=${orderState.name}`
    await fetchDataFromApiWithGet(url)
  }

  async function getFilteredSpendings() {
    console.log(filterState)
    const url = `/api/filter-by-currency?filter-type${filterState.name}`
    await fetchDataFromApiWithGet(url)
  }

  async function fetchDataFromApiWithGet(url){
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" }};

    await fetch(url, requestOptions)
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

import React, {useEffect, useState} from 'react';
import { FiltersWrapper, Orderings, CurrencyFilters, CurrencyButton } from '../styles/ComponentStyles';


export default function CurrencyFilter({ setUrl }) {

  const [orderState, setOrderState] = useState('-spent_at');

  const [filterState, setFilterState] = useState('ALL');

  useEffect ( ()=>{
    setUrl(`http://localhost:8000/api/filter-by-currency?filter-type=${filterState}`)
  }, [filterState])

  useEffect ( ()=>{
    setUrl(`http://localhost:8000/api/order-spendings?order-type=${orderState}`)
  }, [orderState])

  function handleSortingChange(e) {
    setOrderState(e.target.value)
  }

  function handleFilterChange(e) {
    setFilterState(e.target.name)
  }

  return (
    <>
      <FiltersWrapper>
        <Orderings>
          <select onChange={handleSortingChange}>
            <option title='date' value='-spent_at'>Sort by Date descending (default)</option>
            <option title='date' value='spent_at'>Sort by Date ascending</option>
            <option title='amount' value='-amount'>Sort by Amount descending</option>
            <option title='amount' value='amount'>Sort by Amount ascending</option>
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

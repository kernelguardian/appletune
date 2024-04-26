import * as React from 'react'
import Box from '@mui/material/Box'
import Slider from '@mui/material/Slider'

function valuetext(value) {
  return `${value}`
}

const minDistance = 7

export default function RangeSlider(props) {
  let marks = [
    {
      value: 0,
      label: '0:00',
    },
  ]
  for (let i = 0; i < props.maxValue / 60; i++) {
    marks.push({
      value: i * 60,
      label: i + ':00',
    })
  }

  const handleChange1 = (event, newValue, activeThumb) => {
    if (!Array.isArray(newValue)) {
      return
    }

    if (activeThumb === 0) {
      props.setValue1([
        Math.min(newValue[0], props.value1[1] - minDistance),
        props.value1[1],
      ])
    } else {
      props.setValue1([
        props.value1[0],
        Math.max(newValue[1], props.value1[0] + minDistance),
      ])
    }
  }

  return (
    <Box sx={{ width: 500 }}>
      <Slider
        sx={{
          color: '#3a8589',
          height: 3,
          padding: '13px 0',
          '& .MuiSlider-thumb': {
            height: 27,
            width: 27,
            backgroundColor: '#fff',
            border: '1px solid currentColor',
            '&:hover': {
              boxShadow: '0 0 0 8px rgba(58, 133, 137, 0.16)',
            },
            '& .airbnb-bar': {
              height: 9,
              width: 1,
              backgroundColor: 'currentColor',
              marginLeft: 1,
              marginRight: 1,
            },
          },
          '& .MuiSlider-track': {
            height: 3,
          },
          '& .MuiSlider-rail': {
            color: '#d8d8d8',
            opacity: 1,
            height: 3,
          },
        }}
        getAriaLabel={() => 'Minimum distance'}
        value={props.value1}
        scale={(x) => {
          var minutes = Math.floor(x / 60)
          var remainingSeconds = x % 60
          return (
            minutes +
            ':' +
            (remainingSeconds < 10 ? '0' : '') +
            remainingSeconds
          )
        }}
        onChange={handleChange1}
        marks={marks}
        max={props.maxValue}
        getAriaValueText={valuetext}
        valueLabelDisplay="on"
        disableSwap
      />
    </Box>
  )
}

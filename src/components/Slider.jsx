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

import * as React from 'react'
import Box from '@mui/material/Box'
import Slider from '@mui/material/Slider'

function valuetext(value) {
  return `${value}`
}

const minDistance = 7

export default function RangeSlider(props) {
  // const [props.value1, props.setValue1] = React.useState([20, 37])

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
        onChange={handleChange1}
        valueLabelDisplay="auto"
        max={props.maxValue}
        getAriaValueText={valuetext}
        disableSwap
      />
    </Box>
  )
}

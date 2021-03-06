const K_SIZE = 18;

const markerStyle = {
  // initially any map object has left top corner at lat lng coordinates
  // it's on you to set object origin to 0,0 coordinates
  position: 'absolute',
  width: K_SIZE,
  height: K_SIZE,
  left: -K_SIZE / 2,
  top: -K_SIZE / 2,

  border: '1px solid #f44336',
  borderRadius: K_SIZE,
  backgroundColor: 'white',
  textAlign: 'center',
  color: '#3f51b5',
  fontSize: 14,
  fontWeight: 'bold',
  padding: 0,
  cursor: 'pointer',
};

const markerStyleHover = {
  ...markerStyle,
  border: '2px solid #3f51b5',
  color: '#f44336',
};

export { markerStyle, markerStyleHover, K_SIZE };

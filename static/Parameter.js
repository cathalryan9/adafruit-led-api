class Parameter extends React.Component {

       render() {
           console.log(this.props);

        //Need to display parameters properly
          return (
             <div>
             <div>{ this.props.data.input_data.toString()}</div>
             <input></input>
             </div>
          );
       }
}
export default Parameter;

class Layout extends React.Component {


       render() {

        console.log(this.props.page.pageName);
        var contentPages = { "Parameter": Parameter, "File": File };
        console.log(contentPages[this.props.page.pageName]);

        if (this.props.page.pageName in contentPages){
               var Page = React.createElement(contentPages[this.props.page.pageName]);


            }
        //Add else to display not found


          return (
              <div>

                <Header />
                {Page}
                <Footer />
             </div>
          );
       }
}

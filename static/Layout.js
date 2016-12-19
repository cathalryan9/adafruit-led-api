class Layout extends React.Component {

       render() {

        var contentPages = { "Parameter": Parameter, "File": File, "Upload": Upload};

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

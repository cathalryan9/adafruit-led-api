import Header from './Header';
import Footer from './Footer';
import File from './File';
import Parameter from './Parameter';
import Upload from './Upload';

class Layout extends React.Component {

       render() {

        var contentPages = { "Parameter": Parameter, "File": File, "Upload": Upload};
        console.log(this.props.page.pageName);
        if (this.props.page.pageName in contentPages){
               var Page = React.createElement(contentPages[this.props.page.pageName],this.props);
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

export default Layout;
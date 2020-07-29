import React from "react";

const Context = React.createContext();

const reducer = (state, action) => {
    switch (action.type){
        case "DELETE": 
            return  {
                    ...state, 
                    products: state.products.filter(product => product.id !== action.payload)
                }
        case "ADD_PRODUCT":
            return {
                ...state,
                products: [...state.products, action.payload]
            }
        default : 
            return state;
    }

};


export class ProductProvider extends React.Component {
 

    state =  {
        products : [
                     {
                       id: '1',
                       title: 'Iphone 7',
                       src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                       description: 'Good product',
                     },
                     {
                       id: '2',
                       title: 'Iphone 8',
                       src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                       description: 'Good product',
                     },
                     {
                       id: '3',
                       title: 'Iphone 9',
                       src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                       description: 'Good product',
                     },
                     {
                       id: '4',
                       title: 'Iphone 10',
                       src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                       description: 'Good product',
                     },
             ],
             dispatch: action => {
                this.setState(state => reducer(state, action));
            }
     }
    render() {
      const { children } = this.props;
      return ( 
        <Context.Provider value={this.state}>
          {children}
        </Context.Provider>
      );
    }
  }
  
export const ProductConsumer = Context.Consumer;
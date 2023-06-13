import { configureStore } from '@reduxjs/toolkit';
import AllCategoriesSlicer from './Slicers/AllCategorySlicer';
import CategorySlicer from './Slicers/CategorySlicer';
import FoodSlicer from './Slicers/FoodSlicer';

export default configureStore({
    reducer: {
        categories: AllCategoriesSlicer,
        category: CategorySlicer,
        food: FoodSlicer
    },
})
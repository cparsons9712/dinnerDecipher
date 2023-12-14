import { getRecipes } from "../../store/recipe"
import React, { useState , useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";



function RecipeList() {
    const dispatch = useDispatch();

    useEffect (()=>{
        // trigger the data retrieval from the backend to go into the store
        dispatch(getRecipes())
    })

    // save the data in the store to a variable we can use.
    const recipes = useSelector((state) => state.recipes)


    return (
        <h1>Recipes</h1>


    )
}

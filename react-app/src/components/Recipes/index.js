import { getRecipes } from "../../store/recipe"
import React, { useState , useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import './recipe.css';



function RecipeList() {
    const dispatch = useDispatch();

    useEffect (()=>{
        // trigger the data retrieval from the backend to go into the store
        dispatch(getRecipes())
    }, [dispatch])

    // save the data in the store to a variable we can use.
    const recipes = useSelector((state) => state.recipe)
    const recipeArray = Object.values(recipes)

    const formattIngredients = (ingredients) =>{
        return ingredients.split(';')

    }



    return (
    <>
        <h1>Recipes</h1>
        {recipeArray.map((r)=>{
            return (
                <div className="recipeCard">
                    <h2>{r.name}</h2>
                    <p>{r.description}</p>
                    <img src={r.img_url} className="recipeImage" alt={r.name}/>
                    {formattIngredients(r.ingredients).map((r)=>{
                        return (<li>{r}</li>)
                    })}
                    <p>{r.directions}</p>
                </div>
            )
        })}

    </>



    )
}

export default RecipeList

import { getRecipes } from "../../store/recipe"
import React, { useState , useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import './recipe.css';



function CreateUpdateRecipe(recipe) {
    const dispatch = useDispatch();
    const [name, setName] = useState(recipe?.name)
    const [description, setDescription] = useState(recipe?.description)
    const [prepTime, setPrepTime] = useState(recipe?.prepTime)
    const [totalTime, setTotalTime] = useState(recipe?.totalTime)
    const [servings, setServings] = useState(recipe?.servings)
    const [notes, setNotes] = useState(recipe?.notes)
    const [source, setSource] = useState(recipe?.source)
    const [img_url, setImg_Url] = useState(recipe?.img_url)


    useEffect (()=>{
        // trigger the data retrieval from the backend to go into the store
        dispatch(getRecipes())
    }, [dispatch])

    // save the data in the store to a variable we can use.
    const recipes = useSelector((state) => state.recipe)
    const recipeArray = Object.values(recipes)




    return (
    <>
        <h1>{recipe? 'Update' : 'Create'} Recipe</h1>


        <label>
          Title
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>

        <label>
          Description
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>

        <label>
          Prep Time
          <input
            type="text"
            value={prepTime}
            onChange={(e) => setPrepTime(e.target.value)}
          />
        </label>

        <label>
          Total Time
          <input
            type="text"
            value={totalTime}
            onChange={(e) => setTotalTime(e.target.value)}
          />
        </label>

        <label>
          Servings
          <input
            type="text"
            value={servings}
            onChange={(e) => setServings(e.target.value)}
            required
          />
        </label>

        <label>
          Tips & Notes
          <input
            type="text"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
          />
        </label>

        <label>
          Source
          <input
            type="text"
            value={source}
            onChange={(e) => setSource(e.target.value)}
          />
        </label>

        <label>
          Image Url
          <input
            type="text"
            value={img_url}
            onChange={(e) => setImg_Url(e.target.value)}
          />
        </label>





    </>



    )
}

export default RecipeList

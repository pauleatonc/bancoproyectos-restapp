import { useState, useEffect } from 'react';
import apiProjects from '../services/project/projects.api';

const useApiProjectsList = () => {
  const [ dataProject, setDataProject ] = useState([]);
  const [ loadingProject, setLoadingProject ] = useState(true);
  const [ errorProject, setErrorProject ] = useState(null);

  useEffect( ()=>{
    const fetchData = async () => {
      try {
        const response = await apiProjects.get('v1/');
        setDataProject(response.data);
        setLoadingProject(false);
      } catch (error) {
        setErrorProject(error);
        setLoadingProject(false);
      }
    };
    fetchData();
  }, []);

  return { dataProject, loadingProject, errorProject};
}

export default useApiProjectsList;
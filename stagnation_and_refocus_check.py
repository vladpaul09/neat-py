def stagnation_and_refocus_check(population, species_record, stagnation, refocus):
    species_record_nr = len(species_record)
    # Compute mean and max raw fitnesses in each species and store in species_record.generation_record
    max_fitnesses_current_generation = [0 for _ in range(species_record_nr)];

    for index_species in range(species_record_nr):
        if species_record[index_species].number_individuals > 0:
            fitness_species_list = [(individual.species == index_species+1) * individual.fitness for individual in population.genomes]
            max_fitness = max(fitness_species_list)
            index_individual_max = fitness_species_list.index(max_fitness)
            mean_fitness = sum(fitness_species_list) / species_record[index_species].number_individuals
            print(mean_fitness)
            # Compute stagnation vector (last stagnation.number_generation-1 max fitnesses plus current fitness
            if len(species_record[index_species].generation_record) > stagnation.number_generation - 2:
                stagnation_vector = [species_record[index_species].generation_record(3,size(species_record(index_species).generation_record,2)-stagnation.number_generation+2:size(species_record(index_species).generation_record,2)),max_fitness];
   #          # Check for stagnation
   #          if sum(abs(stagnation_vector-mean(stagnation_vector))<stagnation.threshold)==stagnation.number_generation
   #              # Set mean fitness to small value to eliminate species (cannot be set to 0, if only one species is present, we would have divide by zero in fitness sharing. anyways, with only one species present, we have to keep it)
   #             mean_fitness=0.01;
   #          end
   #       end
   #       species_record(index_species).generation_record=[species_record(index_species).generation_record,[generation;mean_fitness;max_fitness;index_individual_max]];
   #       max_fitnesses_current_generation(1,index_species)=max_fitness;
   #    end
   # end
   # %check for refocus
   # [top_fitness,index_top_species]=max(max_fitnesses_current_generation);
   # if size(species_record(index_top_species).generation_record,2)>refocus.number_generation
   #    index1=size(species_record(index_top_species).generation_record,2)-refocus.number_generation;
   #    index2=size(species_record(index_top_species).generation_record,2);
   #    if sum(abs(species_record(index_top_species).generation_record(3,index1:index2)-mean(species_record(index_top_species).generation_record(3,index1:index2)))<refocus.threshold)==refocus.number_generation
   #       [discard,vector_cull]=sort(-max_fitnesses_current_generation);
   #       vector_cull=vector_cull(1,3:sum(max_fitnesses_current_generation>0));
   #       for index_species=1:size(vector_cull,2)
   #          index_cull=vector_cull(1,index_species);
   #          species_record(index_cull).generation_record(2,size(species_record(index_cull).generation_record,2))=0.01;
   #       end
   #    end
   # end

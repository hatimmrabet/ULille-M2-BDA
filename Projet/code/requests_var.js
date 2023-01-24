import {gql} from "@apollo/client";

export const get_probe_nb = gql`
    query top_probe {
        count_probe_name {
            nb_probe
            probe_name
        }
    }
    
`;
const QUERY = gql`
query  {
count_state {
count
state
}
}
`
let typeErrorQuery = gql`
query typeErrorQuery{
kpi_job(where: {type_error: {_eq: "${searchBarValue.slice(1)}"}}) {
                         job_id
                         type_error
                         job_elapsed
                         job_started
                         job_finished
                         fqdn
                         probe_name
                         output_link
                         }
                         }
`;



let ProbeNameQuery = gql`
query probeNameQuery {
kpi_job(where: {probe_name: {_eq: "${searchBarValue.slice(1)}"}}) {
                         job_id
                         type_error
                         job_elapsed
                         job_started
                         job_finished
                         fqdn
                         probe_name
                         output_link
                         }
                         }
`;






export const get_error_number = gql`
    query  {
        count_type_error {
            count
            type_error
        }

    }
`;
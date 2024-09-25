// pipeline {
//   agent any
//   stages {
//     stage('version') {
//       steps {
//         sh 'python3 --version'
//       }
//     }
//     stage('Update xml tag value') {
//       steps {
//         script {
//             // Define the file path, the specific tag, and the new value to set
//             def filePath = '/var/lib/jenkins/jobs/test/jobs/pipeline_automation/builds/4/build.xml'
//             def tag = 'changelogFile'  // No angle brackets here
//             def newValue = '/var/lib/jenkins/jobs/test/jobs/pipeline_automation/builds/4/changelog18258533740849202704.xml'

//             // Run the Python script to update the XML file
//             sh """
//             python3 update_xml.py ${filePath} ${tag} ${newValue}
//             """
//         }
//       }
//     }
    
//   }
// }


pipeline {
    agent any

    stages {
        stage('version') {
          steps {
            sh 'python3 --version'
          }
        }
        stage('Update XML') {
            steps {
                script {
                    def inputFilePath = '/var/lib/jenkins/jobs/test/jobs/pipeline_automation/builds/4/build.xml'
                    def outputFilePath = '/tmp/temp_build.xml'
                    def tagPath = 'changelogFile'
                    def newValue = '/var/lib/jenkins/jobs/test/jobs/pipeline_automation/builds/4/changelog18258533740849202704.xml'

                    // Run the Python script to update the XML file in a temp location
                    sh """
                    python3 update_xml.py ${inputFilePath} ${outputFilePath} ${tagPath} ${newValue}

                    # If the update was successful, move the modified file back to the original location
                    mv ${outputFilePath} ${inputFilePath}
                    """
                }
            }
        }
    }
}

pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      script {
          // Define the file path, the specific tag, and the new value to set
          def filePath = '/var/lib/jenkins/jobs/test/jobs/pipeline_automation/builds/4/build.xml'
          def tag = 'changelogFile'  // No angle brackets here
          def newValue = '/var/lib/jenkins/jobs/test/jobs/pipeline_automation/builds/4/changelog18258533740849202704.xml'

          // Run the Python script to update the XML file
          sh """
          python3 update_xml.py ${filePath} ${tag} ${newValue}
          """
      }
    }
  }
}